"""Customer purchases used by the refund agent.

Dates are intentionally relative to 2026-11-11: a purchase is either
refund-available (at most 30 days old) or expired (more than 30 days old).
"""

users_data = {
    "user123": {
        "book": {"price": 23, "date": "2026-11-05"},  # available
        "pen": {"price": 7, "date": "2026-11-03"},  # available
    },
    "user124": {
        "notebook": {"price": 12, "date": "2026-11-10"},  # available
    },
    "user125": {
        "pencil": {"price": 3, "date": "2026-10-14"},  # available
        "ruler": {"price": 5, "date": "2026-10-10"},  # expired
    },
    "user126": {
        "backpack": {"price": 45, "date": "2026-10-20"},  # available
        "water_bottle": {"price": 18, "date": "2026-10-10"},  # expired
        "lunch_box": {"price": 14, "date": "2026-10-25"},  # available
    },
    "user127": {
        "eraser": {"price": 2, "date": "2026-10-11"},  # expired
    },
    "user128": {
        "stapler": {"price": 11, "date": "2026-10-09"},  # expired
        "highlighter": {"price": 4, "date": "2026-11-08"},  # available
    },
    "user129": {
        "calculator": {"price": 29, "date": "2026-10-10"},  # expired
        "folder": {"price": 6, "date": "2026-10-30"},  # available
        "usb_drive": {"price": 16, "date": "2026-09-27"},  # expired
    },
    "user130": {
        "headphones": {"price": 35, "date": "2026-11-07"},  # available
    },
    "user131": {
        "desk_lamp": {"price": 28, "date": "2026-10-15"},  # available
        "mouse": {"price": 20, "date": "2026-10-05"},  # expired
    },
    "user132": {
        "sketchbook": {"price": 17, "date": "2026-11-02"},  # available
        "paintbrush": {"price": 9, "date": "2026-10-01"},  # expired
        "canvas": {"price": 25, "date": "2026-10-05"},  # expired
    },
}
