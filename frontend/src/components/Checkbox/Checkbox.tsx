import { Check } from "phosphor-react";
import { useState } from "react";

import { CheckboxContainer, CheckboxIndicatorContainer, CheckboxRoot, CheckboxText } from "./styles";

import { Indicator } from '@radix-ui/react-checkbox';

interface Props{
  text: string;
  checked: boolean;
  onCheckChange: () => void
}

export function Checkbox({ text, checked, onCheckChange}: Props){

  const [isChecked, setIsChecked] = useState<boolean>(checked)

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