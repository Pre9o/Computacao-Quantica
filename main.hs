module Main where

import System.Random

-- Definindo um tipo de dados para representar um qubit
data Qubit = Qubit Double Double deriving (Show)

-- Operação de Hadamard em um qubit
hadamard :: Qubit -> Qubit
hadamard (Qubit a b) = Qubit ((a + b) / sqrt 2) ((a - b) / sqrt 2)

-- Medição de um qubit
measure :: Qubit -> IO Int
measure (Qubit a b) = do
  rand <- randomRIO (0.0, 1.0) :: IO Double
  return $ if rand < (a * a) then 0 else 1

main :: IO ()
main = do
  -- Criando um qubit inicializado em |0>
  let qubit0 = Qubit 1 0
  putStrLn "Qubit inicial:"
  print qubit0

  -- Aplicando a operação de Hadamard
  let qubit1 = hadamard qubit0
  putStrLn "Qubit após operação de Hadamard:"
  print qubit1

  -- Medindo o qubit após a operação de Hadamard
  putStrLn "Medição do qubit após operação de Hadamard:"
  measurement <- measure qubit1
  putStrLn $ "Resultado da medição: " ++ show measurement