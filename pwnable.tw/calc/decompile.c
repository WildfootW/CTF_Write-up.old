int calc()
{
  int int_buffer_first; // [sp+18h] [bp-5A0h]@4
  int int_buffer[100]; // [sp+1Ch] [bp-59Ch]@5 400 bits
  char input_buffer; // [sp+1ACh] [bp-40Ch]@2 1024 bits
  int unknown_var; // [sp+5ACh] [bp-Ch]@1

  unknown_var = *MK_FP(__GS__, 20);
  while ( 1 )
  {
    bzero(&input_buffer, 1024u);
    if ( !get_expr((int)&input_buffer, 1024) )
      break;
    init_pool(&int_buffer_first);
    if ( parse_expr((int)&input_buffer, &int_buffer_first) )
    {
      printf((const char *)&unk_80BF804, int_buffer[int_buffer_first - 1]); // printf("%d",)
      fflush(stdout);
    }
  }
  return *MK_FP(__GS__, 20) ^ unknown_var;
}

signed int __cdecl parse_expr(int input_buffer, _DWORD *int_buf_first_adrs)
{
  int number_length; // ST2C_4@3
  signed int result; // eax@4
  int int_buffer_temp_ptr; // eax@6
  int v5; // ebx@25
  int current_input_base; // [sp+20h] [bp-88h]@1
  int i; // [sp+24h] [bp-84h]@1
  int operator_ptr; // [sp+28h] [bp-80h]@1
  char *left_number_string; // [sp+30h] [bp-78h]@3
  int left_number; // [sp+34h] [bp-74h]@5
  char operator_list[100]; // [sp+38h] [bp-70h]@1
  int unknown_var; // [sp+9Ch] [bp-Ch]@1

  unknown_var = *MK_FP(__GS__, 20);
  current_input_base = input_buffer;
  operator_ptr = 0;
  bzero(operator_list, 100u);
  for ( i = 0; ; ++i )
  {
    if ( (unsigned int)(*(_BYTE *)(i + input_buffer) - 48) > 9 )    // not number
    {
      number_length = i + input_buffer - current_input_base;
      left_number_string = (char *)malloc(number_length + 1);
      memcpy(left_number_string, current_input_base, number_length);
      left_number_string[number_length] = 0;
      if ( !strcmp(left_number_string, "0") )
      {
        puts("prevent division by zero");
        fflush(stdout);
        result = 0;
        goto LABEL_25;
      }
      left_number = atoi(left_number_string);
      if ( left_number > 0 )
      {
        int_buffer_temp_ptr = (*int_buf_first_adrs)++;  // save number ptr in int_buffer_first
        int_buf_first_adrs[int_buffer_temp_ptr + 1] = left_number;
      }
      if ( *(_BYTE *)(i + input_buffer) && (unsigned int)(*(_BYTE *)(i + 1 + input_buffer) - 48) > 9 )
      {
        puts("expression error!");
        fflush(stdout);
        result = 0;
        goto LABEL_25;
      }
      current_input_base = i + 1 + input_buffer;
      if ( operator_list[operator_ptr] )
      {
        switch ( *(_BYTE *)(i + input_buffer) )
        {
          case 43:      // +
          case 45:      // -
            eval(int_buf_first_adrs, operator_list[operator_ptr]);
            operator_list[operator_ptr] = *(_BYTE *)(i + input_buffer);
            break;
          case 37:      // %
          case 42:      // *
          case 47:      // /
            if ( operator_list[operator_ptr] != 43 && operator_list[operator_ptr] != 45 )
            {
              eval(int_buf_first_adrs, operator_list[operator_ptr]);
              operator_list[operator_ptr] = *(_BYTE *)(i + input_buffer);
            }
            else
            {
              operator_list[++operator_ptr] = *(_BYTE *)(i + input_buffer);
            }
            break;
          default:
            eval(int_buf_first_adrs, operator_list[operator_ptr--]);
            break;
        }
      }
      else
      {
        operator_list[operator_ptr] = *(_BYTE *)(i + input_buffer);
      }
      if ( !*(_BYTE *)(i + input_buffer) )      // break when null
        break;
    }
  }
  while ( operator_ptr >= 0 )
    eval(int_buf_first_adrs, operator_list[operator_ptr--]);
  result = 1;
LABEL_25:
  v5 = *MK_FP(__GS__, 20) ^ unknown_var;
  return result;
}

_DWORD *__cdecl eval(_DWORD *int_buf_first_adrs, char operator)
{
  _DWORD *result; // eax@12

  if ( operator == 43 )
  {
    int_buf_first_adrs[*int_buf_first_adrs - 1] += int_buf_first_adrs[*int_buf_first_adrs];
  }
  else if ( operator > 43 )
  {
    if ( operator == 45 )
    {
      int_buf_first_adrs[*int_buf_first_adrs - 1] -= int_buf_first_adrs[*int_buf_first_adrs];
    }
    else if ( operator == 47 )
    {
      int_buf_first_adrs[*int_buf_first_adrs - 1] /= int_buf_first_adrs[*int_buf_first_adrs];
    }
  }
  else if ( operator == 42 )
  {
    int_buf_first_adrs[*int_buf_first_adrs - 1] *= int_buf_first_adrs[*int_buf_first_adrs];
  }
  result = int_buf_first_adrs;
  --*int_buf_first_adrs;
  return result;
}

