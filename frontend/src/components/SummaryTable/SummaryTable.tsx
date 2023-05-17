import { HabitDay } from "../HabitDay/HabitDay";
import { WEEKDAYS, generateDatesFromRange } from "../../utils/date";
import { Container, Week, WeekDayName, Heatmap, DayToFill } from "./styles";
import { useEffect, useState } from "react";
import { DayService } from "../../services/DayService";
import dayjs from "dayjs";
import { Day } from "../../interfaces/models";

const summaryDates = generateDatesFromRange()

export function SummaryTable(){

  const [days, setDays] = useState<Day[]>([])
  const amountOfDaysToFill = 7- (summaryDates.length%7)

  useEffect(() => {
    async function listDays(){
      const response = await DayService.listDays()
      setDays(response)
    }
    listDays()
  }, [])
  return(
    <Container>
      <Week>
        {
          WEEKDAYS.map((day, index) =>(
            <WeekDayName key={index}>
              {day[0]}
            </WeekDayName>
          ))
        }
      </Week>
      <Heatmap>
        {days && days.length && summaryDates.map(date => {
          const dayInSummary = days.find(day => {
            return dayjs(date).isSame(day.date, 'day')
          })
          return <HabitDay
                    key={date.toISOString()}
                    date={date}
                    total={dayInSummary?.total}
                    completed={dayInSummary?.completed}
                  />
        })}
        {amountOfDaysToFill > 0 && Array.from({length: amountOfDaysToFill}).map((_, index) => (
          <DayToFill key={index} />
        ))
        }
      </Heatmap>

    </Container>
  )
}