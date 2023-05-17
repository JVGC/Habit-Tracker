import { Check } from "phosphor-react";
import { CheckboxContainer, CheckboxText, CheckboxIndicatorContainer, CheckboxRoot } from "./styles";

import {Indicator} from '@radix-ui/react-checkbox'

interface Props{
  text: string
}

export function Checkbox({text}: Props){
  return (
    <CheckboxContainer>
      <CheckboxRoot>
        <CheckboxIndicatorContainer>
          <Indicator>
            <Check size={20} style={{color: 'white'}}/>
          </Indicator>

        </CheckboxIndicatorContainer>
        <CheckboxText>
          {text}
        </CheckboxText>
      </CheckboxRoot>
    </CheckboxContainer>
  )
}