from fastapi import APIRouter, Depends
from typing import List
from app.src.tests.schemas import STest
from app.src.models import Test
from app.src.tests.dependencies import current_test, all_tests, check_answer

router = APIRouter(
    prefix="/tests",
    tags=["Tests"],
)


@router.get("/", response_model=List[STest])
async def read_tests(skip: int = 0, limit: int = 10, tests: List[Test] = Depends(all_tests)):
    return tests


@router.get("/{test_id}", response_model=STest)
async def read_test(test: Test = Depends(current_test)):
    return test


@router.post("/{test_id}/{question_id}/check-answer")
async def check_answer_endpoint(test_id: int, question_id: int, selected_answer_id: int):
    return await check_answer(test_id, question_id, selected_answer_id)
