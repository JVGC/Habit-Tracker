import { styled } from 'styled-components'


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