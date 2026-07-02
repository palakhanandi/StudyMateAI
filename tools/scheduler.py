def create_schedule(subjects, days):

    schedule = []

    n = len(subjects)

    for i in range(days):

        subject = subjects[i % n]

        schedule.append(
            {
                "Day": i + 1,
                "Subject": subject
            }
        )

    return schedule