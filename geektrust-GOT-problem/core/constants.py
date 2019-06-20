from enum import Enum

KINGDOMS = {
    'land': 'panda',
    'water': 'octopus',
    'ice': 'mammoth',
    'air': 'owl',
    'fire': 'dragon',
    'space': 'gorilla'
}


class ErrorMessages(Enum):
    INVALID_KINGDOM = 'ERROR: Invalid Kingdom: {0}'
    INVALID_MESSAGE = 'ERROR: Invalid Message'
    DUPLICATE_MESSAGE = 'ERROR: Duplicate Message'
