import dayjs from "dayjs"
import { useState, useEffect } from "react"
import { HabitService } from "../../services/HabitService"
import { Checkbox } from "../Checkbox/Checkbox";
import { PopoverContent, PopoverArrow, SelectedDay, ProgressIndicator, SelectedDate, ProgressRoot } from "./styles";

interface Habit {
  id: number;
  name: string;
  start_at: string
}

interface Props {
  date: Date;
  completed: number;
  total: number;
}


export function HabitsList({total, completed, date}: Props){

  const completedPercentage = total > 0 ? Math.round((completed/total) * 100) : 0

  const [habits, setHabits] = useState<Habit[]>([])

  useEffect(() => {
    async function GetDayHabits(){
      const response = await HabitService.listHabits({
        date: dayjs(date).format('YYYY-MM-DD')
      })
      setHabits(response)
    }

    GetDayHabits()

  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  return (
    <PopoverContent>
        <SelectedDay>{dayjs(date).format('dddd')}</SelectedDay>
        <SelectedDate>{dayjs(date).format('DD/MM')}</SelectedDate>

        <ProgressRoot value={completedPercentage}>
        <ProgressIndicator completed={completedPercentage}/>

        </ProgressRoot>

        {habits && habits.map(habit => {
          return <Checkbox key={habit.id} text={habit.name} />
        })}

        <PopoverArrow height={8} width={16}/>
    </ PopoverContent>
  )
}