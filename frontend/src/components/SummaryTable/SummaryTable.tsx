import { HabitDay } from "../HabitDay/HabitDay";
import { WEEKDAYS, generateDatesFromRange } from "../../utils/date";
import { Container, Week, WeekDayName, Heatmap, DayToFill } from "./styles";

const summaryDates = generateDatesFromRange()
const amountOfDaysToFill = 7- (summaryDates.length%7)

export function SummaryTable(){
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
        {summaryDates.map((date, index) => (
          <HabitDay date = {date}total={5} completed={0} key={index}/>
        ))}
        {amountOfDaysToFill > 0 && Array.from({length: amountOfDaysToFill}).map((_, index) => (
          <DayToFill key={index} />
        ))
        }
      </Heatmap>

    </Container>
  )
}