f_whole :: Int -> Int -> Int  -> Int
f_whole  r a b = r * a + b

f_fractional :: Int -> Int -> Double -> Double
f_fractional r a b = fromIntegral(a) + b /fromIntegral(r)



fold_whole :: Int -> [Int] -> Int
fold_whole r = foldl (f_whole r) 0


fold_fractional :: Int -> [Int] -> Double
fold_fractional r lx = x / fromIntegral(r)
  where 
    x = foldr (f_fractional r) 0.0 lx 

-- working version  
fold_to_double  :: Int -> [Int] -> [Int] -> Double
fold_to_double r wx lx = 1.0 * t / k
  where 
    t = fromIntegral (fold_whole r (wx ++ lx)  ) 
    k = fromIntegral(r) ** fromIntegral(length lx)

-- working version by fold two parts separately
fold_to_double2  :: Int -> [Int] -> [Int] -> Double
fold_to_double2 r wx lx | r> 0      = fromIntegral(x) + y 
                                         where 
                                           x = fold_whole r wx 
                                           y = fold_fractional r lx
                        | otherwise = 3


{-

fold_to_double2 10 [-1,2] [3,4]

-}
zero_ones :: Int -> [Int]
zero_ones 0 = [0] ++ zero_ones 1
zero_ones 1 = [1] ++ zero_ones 0

toggle :: Int -> Int
toggle 0 = 1
toggle 1 = 0 



