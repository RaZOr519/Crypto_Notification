SqlConnection connection = new SqlConnection("@");
connection.Open();
SqlCommand cmd = connection.CreateCommand();

cmd.CommandType = CommandType.Text;
cmd.CommandText = "INSERT INTO [TABLE] (eid, name, age, pno) VALUES ('" +id.Text+"', '"+name.Text+"', @Gender)";
cmd.Parameters.AddWithValue("@Gender", Gender);

cmd.ExcuteNonQuery();

connection.Close();
