"""
Career analysis and job role matching logic
"""

from typing import List, Dict, Set
import urllib.parse
# Assuming job_roles_data.py contains the JOB_ROLES_DB dictionary
from backend.data.job_roles_data import JOB_ROLES_DB


def calculate_match_score(user_skills: Set[str], required_skills: List[str]) -> float:
    """
    Calculate match percentage between user skills and required skills
    
    Args:
        user_skills: Set of skills from user's resume
        required_skills: List of skills required for a job role
        
    Returns:
        Match score as percentage (0-100)
    """
    if not required_skills:
        return 0.0
    
    # Convert to lowercase for case-insensitive matching
    user_skills_lower = {skill.lower() for skill in user_skills}
    required_skills_lower = [skill.lower() for skill in required_skills]
    
    # Count matching skills
    matching_skills = sum(1 for skill in required_skills_lower if skill in user_skills_lower)
    
    # Calculate percentage
    match_percentage = (matching_skills / len(required_skills)) * 100
    
    return round(match_percentage, 1)


def analyze_career_fit(user_skills: Set[str]) -> List[Dict]:
    """
    Analyze user skills against all job roles and return ranked matches
    
    Args:
        user_skills: Set of skills from user's resume
        
    Returns:
        List of job role matches sorted by score (highest first)
        Each match contains: role_name, match_score, demand_score, 
        combined_score, description, required_skills, missing_skills
    """
    matches = []
    
    for role_name, role_data in JOB_ROLES_DB.items():
        required_skills = role_data['required_skills']
        match_score = calculate_match_score(user_skills, required_skills)
        demand_score = role_data['demand_score']
        
        # Combined score: 70% match + 30% demand
        combined_score = (match_score * 0.7) + (demand_score * 0.3)
        
        # Identify missing skills
        user_skills_lower = {skill.lower() for skill in user_skills}
        missing_skills = [
            skill for skill in required_skills 
            if skill.lower() not in user_skills_lower
        ]
        
        # Identify known skills
        known_skills = [
            skill for skill in required_skills 
            if skill.lower() in user_skills_lower
        ]
        
        matches.append({
            'role_name': role_name,
            'match_score': match_score,
            'demand_score': demand_score,
            'combined_score': round(combined_score, 1),
            'description': role_data['description'],
            'required_skills': required_skills,
            'known_skills': known_skills, # Key for new feature
            'missing_skills': missing_skills,
            'learning_resources': role_data['learning_resources'],
            'career_path': role_data['career_path']
        })
    
    # Sort by combined score (highest first)
    matches.sort(key=lambda x: x['combined_score'], reverse=True)
    
    return matches


def get_learning_plan(role_match: Dict) -> List[Dict]:
    """
    Generate a learning plan for missing skills
    
    Args:
        role_match: Dictionary containing role match information
        
    Returns:
        List of learning items with skill, resource, and time estimate
    """
    learning_plan = []
    missing_skills = role_match['missing_skills']
    learning_resources = role_match['learning_resources']
    
    # Create a case-insensitive version of learning_resources
    learning_resources_lower = {k.lower(): v for k, v in learning_resources.items()}
    
    for skill in missing_skills:
        skill_lower = skill.lower()
        if skill_lower in learning_resources_lower:
            resource = learning_resources_lower[skill_lower]
            learning_plan.append({
                'skill': skill,
                'youtube_link': resource['youtube'],
                'estimated_hours': resource['estimated_hours']
            })
        else:
            # Fallback for skills without specific resources
            learning_plan.append({
                'skill': skill,
                'youtube_link': f"https://www.youtube.com/results?search_query={skill.replace(' ', '+')}+tutorial",
                'estimated_hours': 30  # Default estimate
            })
    
    return learning_plan


def generate_career_roadmap(role_match: Dict) -> List[str]:
    """
    Generate a career progression roadmap (FIXED to return List[str])
    
    Args:
        role_match: Dictionary containing role match information.
        
    Returns:
        A list of structured strings for the frontend timeline parser.
    """
    career_path_list = role_match.get('career_path', [])
    structured_roadmap = []
    
    for i, step_title in enumerate(career_path_list):
        step_number = i + 1
        
        # Placeholder data for structure
        if step_title.lower().startswith('junior'):
            duration = "1 Year"
            description = "Master core skills from the learning plan. Focus on hands-on execution and seeking continuous mentorship."
            resources = "Internal Team Wiki, Mentor Guidance"
        elif 'mid-level' in step_title.lower() or 'specialist' in step_title.lower():
            duration = "1.5 Years"
            description = "Develop end-to-end ownership of project components. Start participating in architectural and system design decisions."
            resources = "System Design Courses, Advanced Technical Books"
        elif 'senior' in step_title.lower() or 'architect' in step_title.lower():
            duration = "2 Years"
            description = "Drive high-level technical decisions, mentor team members, and focus on long-term system health and scalability."
            resources = "Technical Conference Attendance, Leadership Training"
        elif 'lead' in step_title.lower() or 'manager' in step_title.lower() or 'director' in step_title.lower():
            duration = "Ongoing"
            description = "Transition focus from individual contribution to strategy, team development, and aligning technical goals with business objectives."
            resources = "Management Literature, Executive Coaching"
        else:
            duration = "TBD"
            description = "Continue to grow and seek out new challenges in this stage of your career."
            resources = "N/A"
            
        formatted_step = f"{step_number}. {step_title} [{duration}]: {description}. Resources: {resources}"
        structured_roadmap.append(formatted_step)
        
    return structured_roadmap


def get_job_application_links(role_name: str, known_skills: List[str]) -> List[Dict]:
    """
    Generates direct job application search links for major job boards
    based on the target role and the user's existing skills.
    
    Args:
        role_name: The name of the matched job role.
        known_skills: List of skills the user already has.
        
    Returns:
        A list of dictionaries containing the platform name, URL, and icon.
    """
    
    # 1. Prepare the query: Combine the role name and top 3 relevant skills
    search_terms = [role_name] + known_skills[:3]
    query_string = " ".join(search_terms)
    encoded_query = urllib.parse.quote_plus(query_string)

    # 2. Define the major job board URLs
    links = [
        {
            'platform': 'LinkedIn Jobs',
            # Filtered for jobs posted last week (r604800)
            'url': f"https://www.linkedin.com/jobs/search?keywords={encoded_query}&f_TPR=r604800&sortBy=DD", 
            'icon': '💼'
        },
        {
            'platform': 'Glassdoor',
            'url': f"https://www.glassdoor.com/Job/jobs.htm?sc.keyword={encoded_query}",
            'icon': '🏢'
        },
        {
            'platform': 'Google Jobs',
            # Standard Google search with Jobs filter enabled
            'url': f"https://www.google.com/search?q={encoded_query}&ibp=htl;jobs",
            'icon': '🌐'
        },
    ]
    
    return links