from pydantic import BaseModel


class SLection(BaseModel):
    id: int
    name: str
    course_id: int
    description: str
    file_path: str

    class Config:
        orm_mode = True
        from_attributes = True


class SLectionId(BaseModel):
    id: int

    class Config:
        orm_mode = True
        from_attributes = True
