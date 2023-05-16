import { styled } from 'styled-components'
import { Plus } from 'phosphor-react'


export const Container = styled.div`
  width: 100%;
  max-width: 48rem;
  margin: 0 auto;

  display: flex;
  align-items: center;
  justify-content: space-between;

`

export const Button = styled.button`

  display: flex;
  align-items: center;
  gap: 0.75rem;

  border-width: 2px;
  border-color: #8B5CF6;
  background-color: ${props => props.theme.background};
  font-weight: 600;
  border-radius: 0.5rem;

  padding: 1rem 1.5rem;
  color: white;

  &:hover{
    border-color: #C4B5FD;
  }
`
export const PlusIcon = styled(Plus)`
  color: #8B5CF6;
`