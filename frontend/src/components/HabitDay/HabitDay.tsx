import * as Popover from '@radix-ui/react-popover'

import { PopoverTrigger } from "./styles";
import clsx from 'clsx';
import { HabitsList } from './HabitsList';
import { useState } from 'react';

interface Props {
  date: Date;
  completedStartValue?: number;
  totalInitial?: number;
}


export function HabitDay({date, completedStartValue =0, totalInitial=0}: Props){

  const [completed, setCompleted] = useState(completedStartValue)
  const [total, setTotal] = useState(totalInitial)

  const completedPercentage = total> 0 ? Math.round((completed/total) * 100) : 0

  const onCheckHabit = (newCompletedValue: number, habitsLength: number) => {
    setCompleted(newCompletedValue)
    setTotal(habitsLength)
  }

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
        <HabitsList
          date={date}
          total={total}
          completed={completed}
          onCheckHabit={onCheckHabit}
        />
      </Popover.Portal>
    </Popover.Root>
  )
}