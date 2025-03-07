import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_initial,users_expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ]
        )
    ]
)
def test_restore_names(
        users_initial: list[dict],
        users_expected: list[dict]
) -> None:

    restore_names(users_initial)
    assert users_initial == users_expected
