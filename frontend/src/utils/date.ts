import dayjs from "dayjs";

export function generateDatesFromRange(initialDate = dayjs().startOf('year')): Date[] {
  const firstDayOfTheYear = initialDate

  const today = new Date()
  const dates = []


  let compareDate = firstDayOfTheYear

  while(compareDate.isBefore(today)){
    dates.push(compareDate.toDate())
    compareDate = compareDate.add(1, 'day')
  }

  return dates
}

export const WEEKDAYS = [
  'Sunday',
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday'
]