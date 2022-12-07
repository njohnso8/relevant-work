using DataFrames
using Statistics
using CSV


dow = DataFrame(CSV.File("/Users/noahjohnson/Downloads/relevant-work/Side Projects/Learning New Skills/Julia/Machine Learning Attempt/Data/Processed_DJI.csv"))
nas = DataFrame(CSV.File("/Users/noahjohnson/Downloads/relevant-work/Side Projects/Learning New Skills/Julia/Machine Learning Attempt/Data/Processed_NASDAQ.csv"))
nyse = DataFrame(CSV.File("/Users/noahjohnson/Downloads/relevant-work/Side Projects/Learning New Skills/Julia/Machine Learning Attempt/Data/Processed_NYSE.csv"))
russ = DataFrame(CSV.File("/Users/noahjohnson/Downloads/relevant-work/Side Projects/Learning New Skills/Julia/Machine Learning Attempt/Data/Processed_RUSSELL.csv"))
sp = DataFrame(CSV.File("/Users/noahjohnson/Downloads/relevant-work/Side Projects/Learning New Skills/Julia/Machine Learning Attempt/Data/Processed_S&P.csv"))

dow.id .= "DJI"
nas.id .= "NASDAQ"
nyse.id .= "NYSE"
russ.id .= "RUSSELL"
sp.id .= "S&P"

all_df = dow
names(all_df) == names(nas)
diff_col = findfirst(x -> x == "IXIC", names(all_df))
nas_unique_name = names(nas)[diff_col]
all_df[:,nas_unique_name] .= missing
dow_unique_name = names(all_df)[diff_col]
nas[:, dow_unique_name] .= missing
curr_list = collect(1:(diff_col - 1))
push!(curr_list, size(nas)[2])
append!(curr_list, collect((diff_col + 1):(size(nas)[2] - 1)))
push!(curr_list, diff_col)
nas = nas[!, curr_list]
names(dow) == names(nas)
all_df = [all_df;nas]

ny_diff_col_1 = findfirst(x -> x == "GSPC", names(all_df))
ny_diff_col_2 = findfirst(x -> x == "NYSE", names(all_df))
ny_diff_col_3 = findfirst(x -> x == "RUT", names(all_df))
nyse_unique_name_1 = names(nyse)[ny_diff_col_1]
nyse_unique_name_2 = names(nyse)[ny_diff_col_3]
all_df[:,nyse_unique_name_2] .= missing
all_df_unique_name_1 = names(all_df)[ny_diff_col_1]
all_df_unique_name_2 = names(all_df)[ny_diff_col_2]
nyse[:, all_df_unique_name_1] .= missing
nyse[:, all_df_unique_name_2] .= missing
curr_list = collect(1:(ny_diff_col_1 - 1))
push!(curr_list, (size(nyse)[2]) - 1)
append!(curr_list, collect((ny_diff_col_1 + 1):(ny_diff_col_3 - 1)))
push!(curr_list, ny_diff_col_2)
push!(curr_list, (size(nyse)[2]))
append!(curr_list, collect((ny_diff_col_2 + 1):(size(nyse)[2] - 2)))
push!(curr_list, ny_diff_col_1)
push!(curr_list, ny_diff_col_3)
nyse = nyse[!, curr_list]
names(all_df) == names(nyse)
all_df = [all_df;nyse]

russ_diff_col_1 = findfirst(x -> x == "GSPC", names(all_df))
russ_diff_col_2 = findfirst(x -> x == "RUT", names(all_df))
russ_unique_name_1 = names(russ)[russ_diff_col_1]
nyse_unique_name_2 = names(russ)[russ_diff_col_2]
all_df_unique_name_1 = names(all_df)[russ_diff_col_1]
all_df_unique_name_2 = names(all_df)[russ_diff_col_2]
russ[:, all_df_unique_name_1] .= missing
russ[:, all_df_unique_name_2] .= missing
curr_list = collect(1:(russ_diff_col_1 - 1))
push!(curr_list, (size(russ)[2]) - 1)
append!(curr_list, collect((russ_diff_col_1 + 1):(russ_diff_col_2 - 1)))
push!(curr_list, (size(russ)[2]))
append!(curr_list, collect((russ_diff_col_2 + 1):(size(russ)[2] - 2)))
push!(curr_list, russ_diff_col_1)
push!(curr_list, russ_diff_col_2)
russ = russ[!, curr_list]
names(all_df) == names(russ)
all_df = [all_df;russ]

sp_diff_col = findfirst(x -> x == "GSPC", names(all_df))
sp_unique_name = names(sp)[sp_diff_col]
all_df_unique_name = names(all_df)[sp_diff_col]
all_df_unique_name_end = names(all_df)[end]
sp[:, all_df_unique_name] .= missing
sp[:, all_df_unique_name_end] .= missing
curr_list = collect(1:(sp_diff_col - 1))
push!(curr_list, (size(sp)[2] - 1))
append!(curr_list, collect((sp_diff_col + 1):(size(sp)[2] - 2)))
push!(curr_list, sp_diff_col)
push!(curr_list, size(all_df)[2])
sp = sp[!, curr_list]
names(all_df) == names(sp)
all_df = [all_df;sp]

#Merged dataframe with columns aligned