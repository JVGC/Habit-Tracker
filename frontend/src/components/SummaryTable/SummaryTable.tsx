import { HabitDay } from "../HabitDay/HabitDay";
import { generateDatesFromRange } from "../../utils/date";
import { Container, Week, WeekDayName, Heatmap, DayToFill } from "./styles";

const WEEKDAYS =['D','S', 'T', 'Q', 'Q', 'S', 'S']

const summaryDates = generateDatesFromRange()
const amountOfDaysToFill = summaryDates.length%7 + 1

export function SummaryTable(){
  return(
    <Container>
      <Week>
        {
          WEEKDAYS.map((day, index) =>(
            <WeekDayName key={index}>
              {day}
            </WeekDayName>
          ))
        }
      </Week>
      <Heatmap>
        {summaryDates.map((date, index) => (
          <HabitDay key={index}/>
        ))}
        {amountOfDaysToFill > 0 && Array.from({length: amountOfDaysToFill}).map((_, index) => (
          <DayToFill key={index} />
        ))
        }
      </Heatmap>

    </Container>
  )
}