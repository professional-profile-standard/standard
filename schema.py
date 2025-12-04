from datetime import datetime
from pydantic import BaseModel, HttpUrl, EmailStr


class Location(BaseModel):
    country: str
    state: str | None = None
    city: str | None = None
    village: str | None = None
    street: str | None = None
    postal_code: int | None = None
    address: str | None = None


class Contact(BaseModel):
    country_code: str | None = None
    phone_number: int | None = None
    phone_type: str | None = None
    email: EmailStr | None = None
    website: str | None = None


class PersonalDetails(BaseModel):
    first_name: str
    preferred_first_name: str | None = None
    middle_name: str | None = None
    last_name: str | None = None
    profile_pic: HttpUrl | None = None
    contact: Contact | None = None
    location: str | Location | None = None
    gender: str | None = None
    race: str | None = None


class ProfessionalSummary(BaseModel):
    title: str
    summary: str


class Education(BaseModel):
    institute_name: str
    degree_name: str
    logo: HttpUrl | None = None
    field: str | None = None # cse, ee etc
    subfield: str | None = None
    specialization: str | None = None
    cgpa: str | None = None
    location: str | Location | None = None
    duration: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    achievements: list[str] = []


class Link(BaseModel):
    url: HttpUrl
    name: str | None = None
    url_text: str | None = None


class Experience(BaseModel):
    title: str
    organization: str
    description: str | None = None
    location: str | Location | None = None
    logo: HttpUrl | None = None
    is_current: bool | None = None
    duration: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    experience_type: str | None = None # internship, full-time etc
    contributions: list[str] = []
    achievements: list[str] = []
    technologies: list[str] = [] # the technologies you worked with


class Project(BaseModel):
    name: str
    short_description: str
    description: str | None = None
    type: str | None = None # personal, academic, open-source etc
    links: list[str | Link] = []
    techstack: list[str] = []
    start_date: date | None = None
    end_date: date | None = None
    status: str | None = None # completed, archived etc
    tags: list[str] = []
    details: list[str] = []


class Certificate(BaseModel):
    name: str
    issuer: str
    issue_date: date | None = None
    expiry_date: date| None = None
    credential_id: str | None = None
    url: HttpUrl | None = None
    skills: list[str] = []


class Misc(BaseModel):
    cover_letter: str | None = None
    qna: dict[str, str] = {}
    notes: str | None = None
    others: dict[str, any] | None = None


class Profile(BaseModel):
    professional_summary: ProfessionalSummary
    skills: dict[str, list[str]] = {}
    experiences: list[Experience] = []
    projects: list[Project] = []
    certificates: list[Certificate] = []
    misc: Misc | None = None


class PPS(BaseModel):
    personal_details: PersonalDetails
    educations: list[Education] = []
    links: list[Link]= []
    certificates: list[Certificate] = []
    profiles: dict[str, Profile] = {}
    misc: Misc | None = None
