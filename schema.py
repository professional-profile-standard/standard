from pydantic import BaseModel, Field

class Location(BaseModel):
    country: str
    state: str
    city: str | None = None
    postal_code: int | None = None
    address_line: str | list[str] | None = None

class Contact(BaseModel):
    country_code: str
    phone_number: int
    phone_type: str | None = None
    email: str
    website: str

class ProfessionalSummary(BaseModel):
    title: str
    summary: str

class PersonalDetails(BaseModel):
    first_name: str
    middle_name: str | None = None
    last_name: str
    preferred_first_name: str | None = None
    contact: Contact
    location: str | Location
    gender: str
    race: str

class Education(BaseModel):
    name: str
    location: str | Location
    duration: str | None = None
    from_date: str | None = Field(None, alias="from")
    to: str | None = None
    degree_name: str
    field_of_study: str
    cgpa: str | None = None
    achievements: list[str] | None = None

class Link(BaseModel):
    name: str
    url: str
    url_text: str | None = None

class Experience(BaseModel):
    company_name: str
    location: str | Location
    job_title: str
    currently_work_here: bool | None = None
    duration: str | None = None
    from_date: str | None = Field(None, alias="from")
    to: str | None = None
    contributions: list[str]

class Project(BaseModel):
    name: str
    description: str
    links: list[str | Link]
    techstack: list[str]
    details: list[str]

class Certificate(BaseModel):
    name: str
    number: str
    issuer: str
    link: str | None = None
    issue_date: str | None = None
    expiry_date: str | None = None

class Misc(BaseModel):
    cover_letter: str | None = None
    qnas: dict[str, str]

class Target(BaseModel):
    professional_summary: ProfessionalSummary
    work_experience: list[Experience]
    skills: dict[str, list[str]]
    projects: list[Project]
    certificates: list[Certificate] | None = None
    misc: Misc | None = None

class Resume(BaseModel):
    personal_details: PersonalDetails
    educations: list[Education]
    links: list[Link] | None = None
    targets: dict[str, Target] 
    misc: Misc | None = None
