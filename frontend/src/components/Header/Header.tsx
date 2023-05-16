import { Container, Button, PlusIcon } from './styles'
import logoImage from '../../assets/logo.svg'

export function Header(){
  return (
    <Container>
      <img src={logoImage} alt="logo" />
      <Button type="button">
        <PlusIcon size={20}/>
        New Habit
      </Button>
    </Container>
  )

}