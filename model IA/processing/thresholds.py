# Get thresholds for squat
def get_thresholds_squat():
    _ANGLE_HIP_KNEE_VERT = {
        'NORMAL': (0,  32),
        'TRANS': (35, 65),
        'PASS': (70, 95)
    }

    thresholds = {
        'HIP_KNEE_VERT': _ANGLE_HIP_KNEE_VERT,

        'HIP_THRESH': [10, 50],
        'ANKLE_THRESH': 45,
        'KNEE_THRESH': [50, 70, 95],

        'OFFSET_THRESH': 35.0,
        'INACTIVE_THRESH': 15.0,

        'CNT_FRAME_THRESH': 50

    }

    return thresholds


def get_thresholds_bicepCurls():
    _ELBOW_ANGLE = {
        'EXTENDED': (160, 180),  # Near fully extended arm
        'FLEXED': (0, 60)        # Flexed position
    }

    _REPETITION_PHASES = {
        'START': 160,  # Starting angle for a new repetition
        'END': 60      # End angle for a repetition
    }

    _SHOULDER_MOVEMENT = {
        'MAX_SHIFT': 10  # Maximum allowable shoulder movement in pixels
    }

    _WRIST_ALIGNMENT = {
        'MAX_DEVIATION': 15  # Maximum allowable wrist deviation in degrees
    }

    thresholds = {
        'ELBOW_ANGLE': _ELBOW_ANGLE,
        'REPETITION_PHASES': _REPETITION_PHASES,
        'SHOULDER_MOVEMENT': _SHOULDER_MOVEMENT,
        'WRIST_ALIGNMENT': _WRIST_ALIGNMENT,
        'OFFSET_THRESH': 35.0
    }

    return thresholds


def get_thresholds_shoulderPress():
    _ARM_EXTENSION = {
        'START': (75, 105),  # Starting position, arms bent at about 90 degrees
        'FULL_EXTENSION': (160, 180)  # Arms fully extended overhead
    }

    thresholds = {
        'ARM_EXTENSION': _ARM_EXTENSION,
        'OFFSET_THRESH': 35.0
        # Additional thresholds can be added here if needed
    }

    return thresholds


def get_thresholds_dumbbellLateralRaises():
    _ARM_POSITION = {
        'LOWERED': 0,  # Arms at the sides
        'RAISED': 100   # Arms raised to shoulder height
    }

    thresholds = {
        'ARM_POSITION': _ARM_POSITION,
        'OFFSET_THRESH': 35.0
        # Additional thresholds can be added here if needed
    }

    return thresholds
