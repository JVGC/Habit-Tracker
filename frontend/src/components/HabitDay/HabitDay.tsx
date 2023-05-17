import * as Popover from '@radix-ui/react-popover'

import { ProgressIndicator, ProgressRoot, PopoverArrow, PopoverContent, PopoverTrigger, SelectedDate, SelectedDay } from "./styles";
import dayjs from 'dayjs';
import { WEEKDAYS } from '../../utils/date';
import clsx from 'clsx';
import { Checkbox } from '../Checkbox/Checkbox';
import { useEffect, useState } from 'react';
import { HabitService } from '../../services/HabitService';

interface Props {
  date: Date;
  completed: number;
  total: number;
}

interface Habit {
  id: number;
  name: string;
  start_at: string
}
export function HabitDay({date, completed, total}: Props){

  const [habits, setHabits] = useState<Habit[]>([])

  useEffect(() => {
    async function GetDayHabits(){
      const response = await HabitService.listHabits({
        date: dayjs(date).format('YYYY-MM-DD')
      })
      setHabits(response)
    }

    GetDayHabits()

  })

  const completedPercentage = Math.round((completed/total) * 100)
  return (
    <Popover.Root>
      <PopoverTrigger
        className={clsx({
          'progress-0': completedPercentage===0,
          'progress-0-20': completedPercentage >0 && completedPercentage <20,
          'progress-20-40': completedPercentage >=20 && completedPercentage <40,
          'progress-40-60': completedPercentage >=40 && completedPercentage <60,
          'progress-60-80': completedPercentage >=60 && completedPercentage <80,
          'progress-80-100': completedPercentage >=80
      })}/>
      <Popover.Portal>
        <PopoverContent>
          <SelectedDay>{WEEKDAYS[date.getDay()]}</SelectedDay>
          <SelectedDate>{dayjs(date).format('DD/MM')}</SelectedDate>

          <ProgressRoot value={completedPercentage}>
          <ProgressIndicator completed={completedPercentage}/>

          </ProgressRoot>

          {habits && habits.map(habit => {
            return <Checkbox text={habit.name} />
          })}

          <PopoverArrow height={8} width={16}/>
        </PopoverContent>
      </Popover.Portal>
    </Popover.Root>
  )
}