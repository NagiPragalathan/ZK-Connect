# ZkConnect
An Social Hiring Platform

# Abstract:
In the conventional hiring process, candidate applications are met with limited assessment, leaving the crucial task of evaluating suitability to recruiters. ZKConnect disrupts this norm by introducing a transformative approach. Candidates applying through ZKConnect embark on a journey of unparalleled assessment integrity, beginning with AI-driven, proctored examinations tailored to the role. These exams feature unreplicable automated questions, guaranteeing test security. The results are instantly relayed to recruiters through a real-time leaderboard, accompanied by a comprehensive downloadable report, showcasing the candidate's test performance, resume, and active contributions on LinkedIn and GitHub. ZKConnect empowers recruiters to identify top talent efficiently, with personal interviews reserved for the highest performers. Additionally, a notification plugin enhances communication, ensuring timely updates for candidates and recruiters. ZKConnect represents a paradigm shift, combining advanced technology with human insight to bridge the gap between talent and opportunity, facilitating informed hiring decisions in a competitive job market.

 # ZKConnect

ZKConnect is a revolutionary hiring platform that leverages advanced technology to transform the conventional hiring process. It empowers recruiters to make informed decisions by combining AI-driven assessments, blockchain integration, and real-time communication.

## Features

- **AI-Powered Proctored Examinations:** Customized exams with automated questions ensure test security.
- **Real-Time Leaderboard:** Instantly see top-performing candidates.
- **Comprehensive Candidate Reports:** Detailed reports combining test performance, resume, and contributions.
- **Personal Interviews:** Reserved for high-scoring candidates.
- **Communication Enhancement:** Notification plugin for timely updates.

## Tech Stacks

- **Frontend:** Next.js, HTML , Css
- **Backend:** Python, Node.js (Express)
- **Blockchain Integration:** Web3, Starknet blockchain
- **Database:** MongoDB
- **Decentralized Storage:** StackOS

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (3.x recommended)
- [pip](https://pip.pypa.io/en/stable/installing/)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/installation.html) (recommended for managing dependencies)
- [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (for cloning the repository)

## Clone the Repository

```
git clone https://github.com/NagiPragalathan/ZK-Connect.git
```
## Installation

1. Navigate to the project directory:
    
    `cd ZK-Connect` 
    
2. Create a virtual environment (optional but recommended):
    
    `python -m venv venv` 
    
3. Activate the virtual environment:
    
    - On Windows:
      
        `venv\Scripts\activate` 
        
    - On macOS and Linux:
        
        `source venv/bin/activate` 
        
4. Install project dependencies:
    
    `pip install -r requirements.txt` 
    

## Database Setup

1. Migrate the database:
    
    `python manage.py migrate` 
    
2. Create a superuser (an admin user):
    
    `python manage.py createsuperuser` 
    
3. Run the development server:
4. 
    `python manage.py runserver` 
    

The development server will start, and you can access your Django project at `http://localhost:8000/`.

## Usage

- Access the Django admin panel at `http://localhost:8000/admin/` and log in with the superuser credentials created earlier.
    
- Start building your project by creating Django apps, models, views, and templates.
    
- Customize this README file with your project-specific information.


## Live Version

For a live version of ZKConnect, visit [https://zk-connect.vercel.app/](https://zk-connect.vercel.app/).

## License

This project is licensed under the [MIT License](LICENSE).
