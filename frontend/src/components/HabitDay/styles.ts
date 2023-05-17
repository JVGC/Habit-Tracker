import * as Popover from '@radix-ui/react-popover'
import * as Progress from '@radix-ui/react-progress';
import { styled } from "styled-components";

export const PopoverTrigger = styled(Popover.Trigger)`
  height: 2.5rem;
  width: 2.5rem;

  background-color: #18181B;
  border-width: 2px;
  border-color: #27272A;
  border-radius: 0.5rem;
  cursor: pointer;
`

export const PopoverContent = styled(Popover.Content)`
  min-width: 320px;
  padding: 1.5rem;

  border-radius: 1rem;
  background-color: #18181B;
  display: flex;
  flex-direction: column;
`

export const PopoverArrow = styled(Popover.Arrow)`
  fill: #18181B;
`

export const SelectedDay = styled.span`
  font-weight: 600;
  color: #A1A1AA;

`

export const SelectedDate = styled.span`
  margin-top: 0.25rem;
  font-weight: 800;
  font-size: 1.875rem;
  line-height: 1.25;
`

export const ProgressRoot = styled(Progress.Root)`
  height: 0.75rem;
  border-radius: 0.75rem;
  background-color: #3F3F46;
  width: 100%;
  margin-top: 1rem;
`

export const ProgressIndicator = styled(Progress.Indicator)<{
  completed: number
}>`
  height: 0.75rem;
  border-radius: 0.75rem;

  background-color: #7C3AED;

  width: ${props => props.completed}%;
`