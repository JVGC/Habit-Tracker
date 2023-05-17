import { Check } from "phosphor-react";
import { Form, TitleLabel, SubmitButton, TitleInput,  } from "./styles";

export function NewHabitForm(){
  return (
    <Form action="">

      <TitleLabel htmlFor="title">
        What are you willing to do?
      </TitleLabel>

      <TitleInput
        id="title"
        type="text"
        placeholder="Gym, drink water, meditation..."
        autoFocus
      />

      <SubmitButton type="submit">
        <Check size={20} weight="bold"/>
        Save
      </SubmitButton>
    </Form>
  )
}