import { HabitDay } from "../HabitDay/HabitDay";
import { WEEKDAYS } from "../../utils/date";
import { Container, Week, WeekDayName, Heatmap, DayToFill } from "./styles";
import { useEffect, useState } from "react";
import { DayService } from "../../services/DayService";


interface Day{
  id: number;
  date: string;
  completed: number;
  total: number;
}

export function SummaryTable(){

  const [days, setDays] = useState<Day[]>([])
  const amountOfDaysToFill = 7- (days.length%7)

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
        {days.map((day, index) => (
          <HabitDay date={new Date(day.date)} total={day.total} completed={day.completed} key={index}/>
        ))}
        {amountOfDaysToFill > 0 && Array.from({length: amountOfDaysToFill}).map((_, index) => (
          <DayToFill key={index} />
        ))
        }
      </Heatmap>

    </Container>
  )
}