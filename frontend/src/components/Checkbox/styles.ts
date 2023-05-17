import * as Checkbox from '@radix-ui/react-checkbox'
import { styled } from 'styled-components'

export const CheckboxContainer = styled.div`
  margin-top: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
`

export const CheckboxRoot = styled(Checkbox.Root)`
  display: flex;
  align-items: center;
  gap: 0.75rem;

  border: none;
  background: none;

  &[data-state="checked"] {
    div{
      background-color: #22C55E;
      border: 2px solid #22C55E;
    }
    span{
      text-decoration-line: line-through;
      color: #A1A1AA;
    }
  }
`

export const CheckboxIndicatorContainer = styled.div`
  height: 2rem;
  width: 2rem;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #27272A ;

  cursor: pointer;

  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;

`

export const CheckboxText = styled.span`
  font-size: 1.25rem;
  font-weight: 600;
  color: white;
  line-height: 1.25;
`

