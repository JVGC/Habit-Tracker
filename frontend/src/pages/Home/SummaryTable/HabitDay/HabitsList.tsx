import dayjs from "dayjs";
import { useEffect, useState } from "react";
import { Checkbox } from "../../../../components/Checkbox/Checkbox";
import { HabitService } from "../../../../services/HabitService";
import { PopoverArrow, PopoverContent, ProgressIndicator, ProgressRoot, SelectedDate, SelectedDay } from "./styles";

import { Habit } from "../../../../interfaces/models";
import { DayService } from "../../../../services/DayService";

interface Props {
  date: Date;
  completed: number;
  total: number;
  onCheckHabit: (newCompletedValue: number, habitsLength: number) => void
}


export function HabitsList({total, completed, date, onCheckHabit}: Props){

  const completedPercentage = total > 0 ? Math.round((completed/total) * 100) : 0

  const [habits, setHabits] = useState<Habit[]>([])
  const [completedHabits, setCompletedHabits] = useState<number[]>([])


  useEffect(() => {
    async function GetDayHabits(){
      const response = await HabitService.listHabits({
        date: dayjs(date).format('YYYY-MM-DD')
      })
      setHabits(response)
      const completedHabitInitial = response.filter(habit => habit.completed === true).map(habit => habit.id)
      setCompletedHabits(completedHabitInitial)
    }
    GetDayHabits()
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const onCheckChange = async (habitId: number) => {
    await DayService.checkHabit({habit: String(habitId), date: dayjs(date).format('YYYY-MM-DD')})

    const isHabitAlreadyCompleted = completedHabits.includes(habitId)

    let newCompletedHabits: number[] = []

    if(isHabitAlreadyCompleted){
      newCompletedHabits = completedHabits.filter(id => id !== habitId)
    }else{
      newCompletedHabits = [...completedHabits, habitId]
    }
    setCompletedHabits(newCompletedHabits)
    onCheckHabit(newCompletedHabits.length, habits.length)
  }

  return (
    <PopoverContent>
        <SelectedDay>{dayjs(date).format('dddd')}</SelectedDay>
        <SelectedDate>{dayjs(date).format('DD/MM')}</SelectedDate>

        <ProgressRoot value={completedPercentage}>
        <ProgressIndicator completed={completedPercentage}/>

        </ProgressRoot>

        {habits && habits.map(habit => {
          return <Checkbox
                  key={habit.id}
                  text={habit.name}
                  completed={habit.completed || false}
                  onCheckChange={() => onCheckChange(habit.id)}
                />
        })}

        <PopoverArrow height={8} width={16}/>
    </ PopoverContent>
  )
}