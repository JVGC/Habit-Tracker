import { Container, GlobalStyle } from "./styles/global"
import { Home } from "./pages/Home/Home"

export function App() {

  return (
  <>
    <GlobalStyle />
    <Container>
      <Home />
    </Container>
  </>
  )
}