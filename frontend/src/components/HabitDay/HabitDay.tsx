import * as Popover from '@radix-ui/react-popover'

import { ProgressIndicator, ProgressRoot, PopoverArrow, PopoverContent, PopoverTrigger, SelectedDate, SelectedDay } from "./styles";

const completed =  0
export function HabitDay(){


  return (
    <Popover.Root>
      <PopoverTrigger />
      <Popover.Portal>
        <PopoverContent>
          <SelectedDay>Quarta</SelectedDay>
          <SelectedDate>17/05</SelectedDate>

          <ProgressRoot value={completed}>
          <ProgressIndicator completed={completed}/>

          </ProgressRoot>
          <PopoverArrow height={8} width={16}/>
        </PopoverContent>
      </Popover.Portal>
    </Popover.Root>
  )
}