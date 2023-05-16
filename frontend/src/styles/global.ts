import { styled } from "styled-components";

export const Container = styled.div`
  background-color: ${props => props.theme.background};
  width: 100vw;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
`

export const Home = styled.div`
  width: 100%;
  max-width: 64rem;
  padding: 0rem 1.5rem;

  display: flex;
  flex-direction: column;
  gap: 4rem;

`