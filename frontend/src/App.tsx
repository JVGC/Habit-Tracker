import { Container, Home } from "./styles/global"
import { Header } from "./components/Header/Header"

export function App() {

  return (
    <Container>
      <Home>
        <Header />
      </Home>
    </Container>
  )
}