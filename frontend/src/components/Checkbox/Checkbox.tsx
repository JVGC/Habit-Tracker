import { Check } from "phosphor-react";
import { CheckboxContainer, CheckboxText, CheckboxIndicatorContainer, CheckboxRoot } from "./styles";

import {Indicator} from '@radix-ui/react-checkbox'
import { useState } from "react";

interface Props{
  text: string;
  completed: boolean;
  onCheckChange: () => void
}

export function Checkbox({ text, completed, onCheckChange}: Props){

  const [isChecked, setIsChecked] = useState<boolean>(completed)

  const changeCheckBox = () => {
    setIsChecked(!isChecked)
    onCheckChange()
  }
  return (
    <CheckboxContainer>
      <CheckboxRoot checked={isChecked} onCheckedChange={changeCheckBox}>
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