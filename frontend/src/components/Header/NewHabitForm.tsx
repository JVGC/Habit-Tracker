import { Check } from "phosphor-react";
import { Form, TitleLabel, SubmitButton, TitleInput,  } from "./styles";
import { FormEvent, useState } from "react";
import { HabitService } from "../../services/HabitService";
import dayjs from "dayjs";

export function NewHabitForm(){

  const [title, setTitle] = useState<string>('')

  const createNewHabit = async (e: FormEvent) => {
    e.preventDefault()
    try{
      await HabitService.createNewHabit({title, startAt: dayjs(new Date()).format('YYYY-MM-DD')})
      setTitle('')
    }catch(err){
      console.log(err)
    }
  }
  return (
    <Form onSubmit={createNewHabit}>

      <TitleLabel htmlFor="title">
        What are you willing to do?
      </TitleLabel>

      <TitleInput
        id="title"
        type="text"
        placeholder="Gym, drink water, meditation..."
        autoFocus
        value={title}
        onChange={e => setTitle(e.target.value)}
      />

      <SubmitButton type="submit">
        <Check size={20} weight="bold"/>
        Save
      </SubmitButton>
    </Form>
  )
}