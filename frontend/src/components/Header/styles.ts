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

  border: 2px solid ${props => props.theme.colors.violet['500']};
  background-color: ${props => props.theme.background};
  font-weight: 600;
  border-radius: 0.5rem;

  padding: 1rem 1.5rem;
  color: white;
  cursor: pointer;

  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;

  &:hover{
    border-color: #C4B5FD;
  }
`
export const PlusIcon = styled(Plus)`
  color: ${props => props.theme.colors.violet['500']};
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
  background-color: ${props => props.theme.colors.gray['900']};
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
  color: ${props => props.theme.colors.gray['400']};
  background-color: ${props => props.theme.colors.gray['900']};
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
  background-color: ${props => props.theme.colors.gray['800']};
  border: none;

  color: white;
  &::placeholder{
    color: ${props => props.theme.colors.gray['400']};
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

  background-color: ${props => props.theme.colors.green['600']};
  gap: 0.75rem;
  border: none;

  color: white;

  cursor: pointer;

  transition-property: color, background-color, border-color, text-decoration-color, fill, stroke;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 150ms;


  &:hover{
    background-color: ${props => props.theme.colors.green['500']};
  }

`