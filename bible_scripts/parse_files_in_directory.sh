for filename in OT_yupik_fix/*.txt; do
python parse_by_number.py --i $filename --o $filename.txt
done
