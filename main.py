from datetime import datetime
from argparse import ArgumentParser

parser = ArgumentParser(
    description="Find out elapsed time of a particular type in date range")
parser.add_argument('--start', required=True)
parser.add_argument('--end')
parser.add_argument('--unit', default='second')
parser.add_argument('--config')
parser.add_argument('--preset')

DATE_FMT = '%Y-%m-%d %H:%M:%SZ'

PRESETS = {
    'unfiltered': {},
    '8_hr_workday': {
        'skip': {
            'yearday': [
                # New Year's Day (January 1).
                (1, 1),
            ],
            'weekday': [
                # Weekends
                (6, 7),
            ],
            'month': [
                {
                    1: {
                        'week': [
                            {
                                3: {
                                    # Birthday of Martin Luther King, Jr.
                                    # (Third Monday in January).
                                    'weekday': (1, 1),
                                }
                            }
                        ]
                    },
                    2: {
                        'week': [
                            {
                                3: {
                                    # Washington's Birthday
                                    # (Third Monday in February).
                                    'weekday': (1, 1),
                                }
                            }
                        ]
                    },
                }
            ]
            'weekday_in_week_in_month': [
                (1,)
            ]
        }
    }
}
Memorial Day (Last Monday in May).
Independence Day (July 4).
Labor Day (First Monday in September).
Columbus Day (Second Monday in October).
Veterans Day (November 11).
Thanksgiving Day (Fourth Thursday in November).
Christmas Day (December 25).

def get_time(start, end, unit, config):




if __name__ == '__main__':
    args = parser.parse_args()

    start = datetime.strptime(args.start, DATE_FMT)
    end = datetime.strptime(args.end, DATE_FMT) if args.end else datetime.now()
    unit = args.unit
    config = PRESETS[args.preset] if args.preset else args.config

    print(get_time(start, end, unit, config))
