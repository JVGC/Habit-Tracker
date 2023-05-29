import * as Popover from '@radix-ui/react-popover'
import * as Progress from '@radix-ui/react-progress';
import { styled } from "styled-components";

export const PopoverTrigger = styled(Popover.Trigger)`
  height: 2.5rem;
  width: 2.5rem;

  border-width: 2px;
  border-radius: 0.5rem;

  cursor: pointer;

  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;
`

export const PopoverContent = styled(Popover.Content)`
  min-width: 320px;
  padding: 1.5rem;

  border-radius: 1rem;
  background-color: ${props => props.theme.colors.gray['900']};
  display: flex;
  flex-direction: column;
`

export const PopoverArrow = styled(Popover.Arrow)`
  fill: ${props => props.theme.colors.gray['900']};
`

export const SelectedDay = styled.span`
  font-weight: 600;
  color: ${props => props.theme.colors.gray['400']};

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
  background-color: ${props => props.theme.colors.gray['700']};
  width: 100%;
  margin-top: 1rem;
`

export const ProgressIndicator = styled(Progress.Indicator)<{
  completed: number
}>`
  height: 0.75rem;
  border-radius: 0.75rem;

  background-color: ${props => props.theme.colors.violet['600']};

  width: ${props => props.completed}%;

  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
`