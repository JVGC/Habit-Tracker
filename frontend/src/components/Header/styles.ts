import { styled } from 'styled-components'
import { Plus } from 'phosphor-react'

import * as Dialog from '@radix-ui/react-dialog'

export const Container = styled.div`
  width: 100%;
  max-width: 48rem;
  margin: 0 auto;

  display: flex;
  align-items: center;
  justify-content: space-between;

`

export const DialogTrigger = styled(Dialog.Trigger)`

  display: flex;
  align-items: center;
  gap: 0.75rem;

  border: 2px solid #8B5CF6;
  background-color: ${props => props.theme.background};
  font-weight: 600;
  border-radius: 0.5rem;

  padding: 1rem 1.5rem;
  color: white;
  cursor: pointer;

  &:hover{
    border-color: #C4B5FD;
  }
`
export const PlusIcon = styled(Plus)`
  color: #8B5CF6;
`

export const DialogOverlay = styled(Dialog.Overlay)`
  width: 100vw;
  height: 100vh;
  background-color: black;
  opacity: 0.8;
  position: fixed;
  inset: 0px;

`

export const DialogContent = styled(Dialog.Content)`
  position: absolute;
  padding: 2.5rem;
  background-color: #18181B;
  border-radius: 1rem;
  width: 100%;
  max-width: 28rem;

  top: 50%;
  left: 50%;
  transform: translateX(-50%) translateY(-50%);
`

export const DialogClose = styled(Dialog.Close)`
  position: absolute;
  right: 1.5rem;
  top: 1.5rem;
  color: #A1A1AA;
  background-color: #18181B;
  border: none;
  cursor: pointer;

  &:hover{
    color: #E4E4E7;
  }
`

export const DialogTitle = styled(Dialog.Title)`
  color: white;
  font-size: 1.875rem;
  line-height: 1.25;
  font-weight: 800;

`
export const Form = styled.form`
  width: 100%;
  display: flex;
  flex-direction: column;

  margin-top: 1.5rem;

`

export const TitleLabel = styled.label`

  font-weight: 600;
  line-height: 1.25;
  color: white;

`
export const TitleInput = styled.input`
  padding: 1rem;
  border-radius: 0.5rem;
  margin-top: 0.75rem;
  background-color: #27272A;
  border: none;

  color: white;
  &::placeholder{
    color: #A1A1AA;
  }
`

export const SubmitButton = styled.button`
  margin-top: 1.5rem;
  border-radius: 0.5rem;
  padding: 1rem;

  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;

  background-color: #16A34A;
  gap: 0.75rem;
  border: none;

  color: white;


  &:hover{
    background-color: #22C55E;
  }

`