# Professional Profile Specification

**Draft**

A standard for professional details.

This specification is a structured yml file containing all professional
details of individual. Professional details such as experience, education,
skills etc are part of this specification.

## Spec

**Personal details**

- `first_name`
- `preferred_first_name`
- `middle_name` 
- `last_name` 

**Contact information**

- `location`
- `country_name`
- `country_code`
- `phone_number`
- `email`
- `linkedin`
- `github`
- `website`

**Experience**
- company\_name
- location
- role
- duration
- contributions

**education**

- name
- location
- duration
- degree\_name
- cgpa
- achievements

**salary**

- 

**misc**

- `cover_letter`

### Skills

- languages



**Company specific**

- `qna`

## Example

```yml
personal_details:
  first_name: Md
  middle_name: Sujauddin
  last_name: Sekh
  preferred_first_name: Sujauddin
  gender: Male
  race: Indian
  location: West Bengal, India
  contact:
    country_code: "+91"
    phone_number: 9999999999 
    email: ssujj@protonmail.com
    website: https://sujauddin.me

educations:
  - name: Narula Institute of Technology
    location: West Bengal, India
    from: "2021"
    to: "2025"
    degree_name: B.Tech.
    field_of_study: "Computer Science Engineering (Specialization in AIML)"
    achievements:
      - Ranked 2nd in debugging competition

links:
  - name: Leetcode
    url: https://leetcode.com/sujaudd1n
    url_text: leetcode.com/sujaudd1n
  - name: Github
    url: https://github.com/sujaudd1n
    url_text: github.com/sujaudd1n
  - name: Linkedin
    url: https://linkedin.com/in/sujaudd1n
    url_text: linkedin.com/in/sujaudd1n
  - name: sujauddin.me/articles
    url: https://sujauddin.me/articles
    url_text: sujauddin.me/articles

targets:
  swe:
    professional_summary:
      title: Junior Software Engineer
      summary: >
        Aspiring software engineer with experience in designing and developing full-stack AI-integrated applications. As an engineering intern,
        I contributed to software projects, leveraging technical expertise to drive innovative solutions and tackle complex real-world problems.
    skills:
      languages: [Python, JavaScript, C, C++, SQL, HTML, CSS]
      libraries: [React, NextJS, Django, FastAPI, Replicate]
      'Protocols & APIs': [HTTP, REST APIs, OAuth, OIDC, OpenAPI]
      Databases: [SQLite, PostgreSQL, MongoDB]
      Tools: [Git, BASH, Virtual Machine, Docker]
      Experience: [Linux, Algorithms, Fullstack Development, Open Source, CI/CD, Agile, Object Oriented Programming, GenAI, Machine Learning]
    
    work_experience:
      - company_name: Genovation Solutions
        location: West Bengal, India
        job_title: Junior Backend Developer Intern
        from: Jul 2025
        to: Sep 2025
        contributions:
          - Engineered a scalable backend system for IoT applications, featuring a real-time database that facilitated seamless data ingestion and processing.
          - Integrated Large Language Models (LLMs) to automate data interpretation, enhancing data comprehension and actionable insights by 50%.
          - Developed and deployed full-stack AI applications using technologies like FastAPI, Replicate, Gradio, and Streamlit, ensuring robust performance and user-friendly interfaces.
          - Successfully migrated a Gradio application to Streamlit, improving maintainability and deployment flexibility while preserving all original UI components and functionality.
          - Boosted research output by implementing integration between autonomous AI agents.
      - company_name: Zapuza Technologies
        location: West Bengal, India
        job_title: Junior Python Developer Intern
        from: Nov 2024
        to: Apr 2025
        contributions:
          - Enhanced employee management by integrating attendance tracking with location-based monitoring, resulting in a 20% increase in system functionality and streamlined administrative processes.
          - Improved data-driven decision-making by designing and developing a financial dashboard that delivered a 40% enhancement in data visualization, enabling quicker insights.
          - Fortified project security by implementing a role-based access control system, ensuring secure authorization and authentication protocols to protect sensitive data, mitigating potential breaches.
    projects:
      - name: QuickNote
        description: AI-powered article writer SaaS.
        links:
          - https://makequicknote.vercel.app
        techstack: [Python, Django, NextJS, GeminiAI]
        details:
          - Developed a cutting-edge SaaS platform for productivity, leveraging AI-driven technology to generate high-quality PDF articles from user-provided topics or prompts.
          - Utilized Amazon S3 cloud storage to store and serve generated PDF files, ensuring secure and efficient data management.
          - Successfully integrated Gemini’s GenAI capabilities to power the article creation process, enabling users to access high-quality, AI-generated content.

misc:
  qnas:
    'Can you relocate?': 'Yes'
    'What is your preferred location?': Remote
         
```

This spec aims to simplify job searching process for job seeker.

## Tooling

To test this spec, use the following yml spec and the frontend.

Spec YML: 
Frontend: 

The source code of these tools can be found at github.com/professional-profile-standard
