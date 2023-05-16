import { Check } from "phosphor-react";
import { Form, TitleLabel, RecurrenceLabel, SubmitButton, TitleInput,  } from "./styles";

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

      <RecurrenceLabel htmlFor="">
        What is the recurrence?
      </RecurrenceLabel>

      <SubmitButton type="submit">
        <Check size={20} weight="bold"/>
        Save
      </SubmitButton>
    </Form>
  )
}