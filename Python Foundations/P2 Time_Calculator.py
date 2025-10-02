def to_minutes(hour, minute, period):
    """Convert 12-hour clock time into total minutes since midnight."""
    # Convert PM hours (except 12 PM) to 24-hour format
    if period == 'PM' and hour != 12:
        hour += 12
    # Convert 12 AM to 0 hours
    elif period == 'AM' and hour == 12:
        hour = 0
    return hour * 60 + minute


def to_12_hour(hour, minute):
    """Convert 24-hour format time back into 12-hour format with AM/PM."""
    # Decide AM/PM
    if hour >= 12:
        period = "PM"
    else:
        period = "AM"

    # Handle special cases for 12-hour conversion
    if hour == 0:
        hour = 12           # midnight (0 → 12 AM)
    elif hour > 12:
        hour -= 12          # convert hours >12 into 12-hour format
    
    # Format minutes with leading zero if needed
    return f"{hour}:{minute:02d} {period}"


def calculate_final_day(starting_day, days_later):
    """Find the final day of the week after adding days_later to starting_day."""
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    # Normalize case (e.g., "tueSday" → "Tuesday")
    starting_day_index = days_of_week.index(starting_day.capitalize())
    
    # Wrap around the week using modulo
    final_day_index = (starting_day_index + days_later) % 7
    
    return days_of_week[final_day_index]


def add_time(start, duration, starting_day=None):
    """
    Add a duration to a start time (12-hour format) and return the new time.
    
    Arguments:
      start: str, start time in 'H:MM AM/PM' format
      duration: str, duration in 'H:MM' format
      starting_day: str (optional), starting day of the week
    
    Returns:
      str, the new time with optional day info and number of days later
    """
    
    # Split start time into components
    start_time = start.split()   # e.g. ['3:00', 'PM']
    start_hour, start_minute = map(int, start_time[0].split(':'))
    start_period = start_time[1]

    # Split duration into hours and minutes
    duration_hour, duration_minute = duration.split(':')

    # Convert both times into total minutes
    start_total_minutes = to_minutes(start_hour, start_minute, start_period)
    duration_total_minutes = int(duration_hour) * 60 + int(duration_minute)

    # Add duration to start
    end_total_minutes = start_total_minutes + duration_total_minutes

    # Convert back to hours and minutes (24-hour format)
    end_hour_24 = (end_total_minutes // 60) % 24
    end_minute = end_total_minutes % 60

    # Format into 12-hour clock
    final_time = to_12_hour(end_hour_24, end_minute)

    # Calculate how many days later the result is
    days_later = end_total_minutes // (24 * 60)

    # Case 1: If starting_day is provided
    if starting_day:
        final_day = calculate_final_day(starting_day, days_later)
        
        if days_later == 0:
            return f"{final_time}, {final_day}"
        elif days_later == 1:
            return f"{final_time}, {final_day} (next day)"
        else:
            return f"{final_time}, {final_day} ({days_later} days later)"
    
    # Case 2: No starting_day provided
    else:
        if days_later == 0:
            return final_time
        elif days_later == 1:
            return f"{final_time} (next day)"
        else:
            return f"{final_time} ({days_later} days later)"


# Example runs
if __name__ == "__main__":
    print(add_time("3:00 PM", "3:10", "Monday"))  
    print(add_time("11:30 AM", "2:32", "Monday"))  
    print(add_time("11:43 AM", "00:20", "Tuesday"))  
    print(add_time("10:10 PM", "3:30"))  
    print(add_time("11:43 PM", "24:20", "tueSday"))  
    print(add_time("6:30 PM", "205:12"))  
    print(add_time("8:16 PM", "466:02", "tuesday"))  
