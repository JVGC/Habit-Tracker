import * as Popover from '@radix-ui/react-popover';
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