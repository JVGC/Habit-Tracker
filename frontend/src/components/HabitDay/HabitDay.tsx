import * as Popover from '@radix-ui/react-popover'

import { PopoverTrigger } from "./styles";
import clsx from 'clsx';
import { HabitsList } from './HabitsList';

interface Props {
  date: Date;
  completedStartValue?: number;
  total?: number;
}


export function HabitDay({date, completedStartValue=0, total=0}: Props){

  const completedPercentage = total > 0 ? Math.round((completedStartValue/total) * 100) : 0

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
          completed={completedStartValue}
        />
      </Popover.Portal>
    </Popover.Root>
  )
}