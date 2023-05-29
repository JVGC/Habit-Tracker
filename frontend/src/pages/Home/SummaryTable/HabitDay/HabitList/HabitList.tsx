import dayjs from "dayjs";
import { useEffect, useState } from "react";
import { Checkbox } from "../../../../../components/Checkbox/Checkbox";
import { Habit } from "../../../../../interfaces/models";
import { DayService } from "../../../../../services/DayService";
import { HabitService } from "../../../../../services/HabitService";
import {
    PopoverArrow,
    PopoverContent,
    ProgressIndicator,
    ProgressRoot,
    SelectedDate,
    SelectedDay
} from "./styles";


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
    async function getDayHabits(){
      try{
        const tempHabits = await HabitService.listHabits({
          date: dayjs(date).format('YYYY-MM-DD')
        })
        setHabits(tempHabits)
        const tempCompletedHabits = tempHabits.filter(
          habit => habit.completed === true
        ).map(
          habit => habit.id
        )
        setCompletedHabits(tempCompletedHabits)
      }catch(error){
        console.log(error)
      }
    }
    getDayHabits()
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const onCheckChange = async (habitId: number) => {
    try{
      await DayService.checkHabit({
        habit: String(habitId),
        date: dayjs(date).format('YYYY-MM-DD')
      })
      const isHabitAlreadyCompleted = completedHabits.includes(habitId)
      let newCompletedHabits: number[] = []

      if(isHabitAlreadyCompleted){
        newCompletedHabits = completedHabits.filter(id => id !== habitId)
      }else{
        newCompletedHabits = [...completedHabits, habitId]
      }
      setCompletedHabits(newCompletedHabits)
      onCheckHabit(newCompletedHabits.length, habits.length)
    }catch(error){
      console.log(error)
    }
  }

  return (
    <PopoverContent side="left">
        <SelectedDay>{dayjs(date).format('dddd')}</SelectedDay>
        <SelectedDate>{dayjs(date).format('MM/DD')}</SelectedDate>

        <ProgressRoot value={completedPercentage}>
          <ProgressIndicator completed={completedPercentage}/>
        </ProgressRoot>

        {habits && habits.map(habit => {
          return <Checkbox
                  key={habit.id}
                  text={habit.name}
                  checked={habit.completed || false}
                  onCheckChange={() => onCheckChange(habit.id)}
                />
        })}

        <PopoverArrow height={8} width={16}/>
    </ PopoverContent>
  )
}