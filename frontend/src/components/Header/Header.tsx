import * as Dialog from '@radix-ui/react-dialog'

import { Container, DialogTrigger, PlusIcon, DialogContent, DialogOverlay, DialogClose, DialogTitle } from './styles'
import logoImage from '../../assets/logo.svg'
import { X } from 'phosphor-react'
import { NewHabitForm } from './NewHabitForm'

export function Header(){
  return (
    <Container>
      <img src={logoImage} alt="logo" />

      <Dialog.Root>

      <DialogTrigger  type="button">
        <PlusIcon size={20}/>
        New Habit
      </DialogTrigger>
      <Dialog.Portal>
        <DialogOverlay />
        <DialogContent>
          <DialogClose>
            <X size={24} aria-label='close'/>
          </DialogClose>
          <DialogTitle>
            Add New Habit
          </DialogTitle>
          <NewHabitForm />
        </DialogContent>
      </Dialog.Portal>
      </Dialog.Root>
    </Container>
  )

}