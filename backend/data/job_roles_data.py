"""
Static job roles database with skills, demand scores, and learning resources
"""

JOB_ROLES_DB = {
    "Data Analyst": {
        "required_skills": [
            "SQL", "Excel", "Python", "Data Visualization", "Statistics",
            "Tableau", "Power BI", "Data Cleaning", "Business Intelligence"
        ],
        "demand_score": 85,
        "description": "Analyze data to help businesses make informed decisions",
        "learning_resources": {
            "SQL": {
                "youtube": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
                "estimated_hours": 40
            },
            "Python": {
                "youtube": "https://www.youtube.com/watch?v=r-uOLxNrNk8",
                "estimated_hours": 60
            },
            "Data Visualization": {
                "youtube": "https://www.youtube.com/watch?v=a9UrKTVEeZA",
                "estimated_hours": 30
            },
            "Tableau": {
                "youtube": "https://www.youtube.com/watch?v=aHaOIvR00So",
                "estimated_hours": 25
            },
            "Statistics": {
                "youtube": "https://www.youtube.com/watch?v=xxpc-HPKN28",
                "estimated_hours": 50
            },
            "Excel": {
                "youtube": "https://www.youtube.com/watch?v=Vl0H-qTclOg",
                "estimated_hours": 20
            },
            "Power BI": {
                "youtube": "https://www.youtube.com/watch?v=3u7Z2v9o_iA",
                "estimated_hours": 30
            },
            "Data Cleaning": {
                "youtube": "https://www.youtube.com/watch?v=h3Y_qodr4_8",
                "estimated_hours": 15
            },
            "Business Intelligence": {
                "youtube": "https://www.youtube.com/watch?v=A_y-9W_a4-c",
                "estimated_hours": 25
            }
        },
        "career_path": ["Junior Data Analyst", "Data Analyst", "Senior Data Analyst", "Data Scientist"]
    },
    
    "Data Scientist": {
        "required_skills": [
            "Python", "R", "Machine Learning", "Statistics", "SQL",
            "Deep Learning", "Data Visualization", "Pandas", "NumPy", "Scikit-learn"
        ],
        "demand_score": 92,
        "description": "Build predictive models and extract insights from complex data",
        "learning_resources": {
            "Machine Learning": {
                "youtube": "https://www.youtube.com/watch?v=GwIo3gDZCVQ",
                "estimated_hours": 100
            },
            "Deep Learning": {
                "youtube": "https://www.youtube.com/watch?v=Z_ikDlimN6A",
                "estimated_hours": 80
            },
            "Python": {
                "youtube": "https://www.youtube.com/watch?v=WGJJIrtnfpk",
                "estimated_hours": 60
            },
            "Statistics": {
                "youtube": "https://www.youtube.com/watch?v=zouPoc49xbk",
                "estimated_hours": 50
            },
            "Scikit-learn": {
                "youtube": "https://www.youtube.com/watch?v=pqNCD_5r0IU",
                "estimated_hours": 40
            },
            "R": {
                "youtube": "https://www.youtube.com/watch?v=1_v_b_GC-c4",
                "estimated_hours": 50
            },
            "Pandas": {
                "youtube": "https://www.youtube.com/watch?v=vmEHCJofslg",
                "estimated_hours": 40
            },
            "NumPy": {
                "youtube": "https://www.youtube.com/watch?v=QUT1VHiLmmI",
                "estimated_hours": 30
            }
        },
        "career_path": ["Data Analyst", "Junior Data Scientist", "Data Scientist", "Senior Data Scientist", "ML Engineer"]
    },
    
    "ML Engineer": {
        "required_skills": [
            "Python", "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch",
            "MLOps", "Docker", "Kubernetes", "Cloud Platforms", "Model Deployment"
        ],
        "demand_score": 88,
        "description": "Design and deploy machine learning systems at scale",
        "learning_resources": {
            "TensorFlow": {
                "youtube": "https://www.youtube.com/watch?v=tPYj3fFJGjk",
                "estimated_hours": 60
            },
            "PyTorch": {
                "youtube": "https://www.youtube.com/watch?v=c36lUUr864M",
                "estimated_hours": 60
            },
            "MLOps": {
                "youtube": "https://www.youtube.com/watch?v=9BgIDqAzfuA",
                "estimated_hours": 50
            },
            "Docker": {
                "youtube": "https://www.youtube.com/watch?v=fqMOX6JJhGo",
                "estimated_hours": 30
            },
            "Model Deployment": {
                "youtube": "https://www.youtube.com/watch?v=f6jAz1zyrDI",
                "estimated_hours": 40
            },
            "Cloud Platforms": {
                "youtube": "https://www.youtube.com/watch?v=3hLmDS179YE",
                "estimated_hours": 32
            }
        },
        "career_path": ["Data Scientist", "Junior ML Engineer", "ML Engineer", "Senior ML Engineer", "AI Architect"]
    },
    
    "Software Engineer": {
        "required_skills": [
            "Python", "Java", "JavaScript", "Git", "Data Structures",
            "Algorithms", "SQL", "REST APIs", "Testing", "Agile"
        ],
        "demand_score": 90,
        "description": "Design, develop, and maintain software applications",
        "learning_resources": {
            "Data Structures": {
                "youtube": "https://www.youtube.com/watch?v=RBSGKlAvoiM",
                "estimated_hours": 80
            },
            "Algorithms": {
                "youtube": "https://www.youtube.com/watch?v=0IAPZzGSbME",
                "estimated_hours": 80
            },
            "Java": {
                "youtube": "https://www.youtube.com/watch?v=eIrMbAQSU34",
                "estimated_hours": 70
            },
            "REST APIs": {
                "youtube": "https://www.youtube.com/watch?v=7YcW25PHnAA",
                "estimated_hours": 30
            },
            "Git": {
                "youtube": "https://www.youtube.com/watch?v=RGOj5yH7evk",
                "estimated_hours": 20
            },
            "Python": {
                "youtube": "https://www.youtube.com/watch?v=WGJJIrtnfpk",
                "estimated_hours": 60
            },
            "JavaScript": {
                "youtube": "https://www.youtube.com/watch?v=PkZNo7MFNFg",
                "estimated_hours": 60
            },
            "Testing": {
                "youtube": "https://www.youtube.com/watch?v=G4jY9c9Gf5E",
                "estimated_hours": 10
            },
            "Agile": {
                "youtube": "https://www.youtube.com/watch?v=3sOe_a-7-iA",
                "estimated_hours": 2
            }
        },
        "career_path": ["Junior Software Engineer", "Software Engineer", "Senior Software Engineer", "Tech Lead", "Engineering Manager"]
    },
    
    "Full Stack Developer": {
        "required_skills": [
            "JavaScript", "React", "Node.js", "HTML", "CSS",
            "MongoDB", "SQL", "REST APIs", "Git", "TypeScript"
        ],
        "demand_score": 87,
        "description": "Build complete web applications from frontend to backend",
        "learning_resources": {
            "React": {
                "youtube": "https://www.youtube.com/watch?v=bMknfKXIFA8",
                "estimated_hours": 50
            },
            "Node.js": {
                "youtube": "https://www.youtube.com/watch?v=Oe421EPjeBE",
                "estimated_hours": 50
            },
            "JavaScript": {
                "youtube": "https://www.youtube.com/watch?v=PkZNo7MFNFg",
                "estimated_hours": 60
            },
            "MongoDB": {
                "youtube": "https://www.youtube.com/watch?v=-56x56UppqQ",
                "estimated_hours": 30
            },
            "TypeScript": {
                "youtube": "https://www.youtube.com/watch?v=BwuLxPH8IDs",
                "estimated_hours": 40
            },
            "HTML": {
                "youtube": "https://www.youtube.com/watch?v=G3e-cpL7ofc",
                "estimated_hours": 4
            },
            "CSS": {
                "youtube": "https://www.youtube.com/watch?v=OliE1s_m3fI",
                "estimated_hours": 11
            },
            "SQL": {
                "youtube": "https://www.youtube.com/watch?v=HXV3zeQKqGY",
                "estimated_hours": 40
            }
        },
        "career_path": ["Junior Full Stack Developer", "Full Stack Developer", "Senior Full Stack Developer", "Tech Lead"]
    },
    
    "DevOps Engineer": {
        "required_skills": [
            "Linux", "Docker", "Kubernetes", "CI/CD", "AWS",
            "Terraform", "Ansible", "Git", "Python", "Monitoring"
        ],
        "demand_score": 86,
        "description": "Automate and optimize software development and deployment processes",
        "learning_resources": {
            "Docker": {
                "youtube": "https://www.youtube.com/watch?v=pTFZFxd4hOI",
                "estimated_hours": 40
            },
            "Kubernetes": {
                "youtube": "https://www.youtube.com/watch?v=X48VuDVv0do",
                "estimated_hours": 60
            },
            "AWS": {
                "youtube": "https://www.youtube.com/watch?v=3hLmDS179YE",
                "estimated_hours": 80
            },
            "Terraform": {
                "youtube": "https://www.youtube.com/watch?v=SLB_c_ayRMo",
                "estimated_hours": 40
            },
            "CI/CD": {
                "youtube": "https://www.youtube.com/watch?v=R8_veQiYBjI",
                "estimated_hours": 35
            },
            "Linux": {
                "youtube": "https://www.youtube.com/watch?v=sWbUDq4S6Y8",
                "estimated_hours": 4
            },
            "Ansible": {
                "youtube": "https://www.youtube.com/watch?v=1n-0o_f_e0g",
                "estimated_hours": 5
            },
            "Monitoring": {
                "youtube": "https://www.youtube.com/watch?v=g_GG-A5d2cM",
                "estimated_hours": 1
            }
        },
        "career_path": ["Junior DevOps Engineer", "DevOps Engineer", "Senior DevOps Engineer", "DevOps Architect"]
    },
    
    "Business Analyst": {
        "required_skills": [
            "Business Intelligence", "SQL", "Excel", "Requirements Analysis", "JIRA",
            "Process Modeling", "Stakeholder Management", "Data Analysis", "Documentation"
        ],
        "demand_score": 82,
        "description": "Bridge business needs with technical solutions",
        "learning_resources": {
            "Business Intelligence": {
                "youtube": "https://www.youtube.com/watch?v=26GlYqgxQ_E",
                "estimated_hours": 50
            },
            "Requirements Analysis": {
                "youtube": "https://www.youtube.com/watch?v=tUvFrxxpAXI",
                "estimated_hours": 40
            },
            "SQL": {
                "youtube": "https://www.youtube.com/watch?v=1YcD1wz5Qpk",
                "estimated_hours": 40
            },
            "Process Modeling": {
                "youtube": "https://www.youtube.com/watch?v=YG-_EXKhK8M",
                "estimated_hours": 30
            },
            "JIRA": {
                "youtube": "https://www.youtube.com/watch?v=nHuhojfjeUY",
                "estimated_hours": 20
            },
            "Excel": {
                "youtube": "https://www.youtube.com/watch?v=Vl0H-qTclOg",
                "estimated_hours": 20
            },
            "Data Analysis": {
                "youtube": "https://www.youtube.com/watch?v=h3Y_qodr4_8",
                "estimated_hours": 15
            },
            "Stakeholder Management": {
                "youtube": "https://www.youtube.com/watch?v=0_jZtny4-eQ",
                "estimated_hours": 1
            },
            "Documentation": {
                "youtube": "https://www.youtube.com/watch?v=B6y_p5qXb-A",
                "estimated_hours": 1
            }
        },
        "career_path": ["Junior Business Analyst", "Business Analyst", "Senior Business Analyst", "Product Manager"]
    }
}

# Common technical skills for keyword extraction
COMMON_SKILLS = [
    # Programming Languages
    "Python", "Java", "JavaScript", "C++", "C#", "R", "Go", "Ruby", "PHP", "Swift",
    "Kotlin", "TypeScript", "Scala", "Rust", "MATLAB",
    
    # Web Technologies
    "HTML", "CSS", "React", "Angular", "Vue.js", "Node.js", "Django", "Flask",
    "Express.js", "Spring Boot", "REST APIs", "GraphQL",
    
    # Databases
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "Redis", "Oracle", "NoSQL",
    "Cassandra", "DynamoDB",
    
    # Data Science & ML
    "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Scikit-learn",
    "Pandas", "NumPy", "Data Visualization", "Statistics", "NLP", "Computer Vision",
    
    # Cloud & DevOps
    "AWS", "Azure", "GCP", "Docker", "Kubernetes", "CI/CD", "Jenkins", "Git",
    "Terraform", "Ansible", "Linux", "MLOps",
    
    # Analytics & BI
    "Tableau", "Power BI", "Excel", "Data Analysis", "Business Intelligence",
    "Data Cleaning", "ETL",
    
    # Other
    "Agile", "Scrum", "JIRA", "Testing", "Debugging", "Problem Solving",
    "Communication", "Team Collaboration", "Project Management"
]