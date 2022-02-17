DECLARE @d date =  DATEADD(m , -6 , GETDATE())
SET @d = DATEADD(d , 1-DAY(@d) , @d)

SELECT ps.Id as post_id, ps.ParentId as parent_id, ps.Title as Title, 
       ps.Body as post_text, cm.Id as com_id, cm.Text as com_text,
       cm.UserId as com_user_id, us.Reputation as reputation,
       ps.CreationDate as dt
FROM Posts as ps
  INNER JOIN Comments as cm ON cm.PostId = ps.Id
  INNER JOIN Users as us ON us.Id = cm.UserId
  
WHERE ps.CreationDate>=@d and cm.CreationDate>=@d