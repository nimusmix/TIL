# React_10_react-hook-form

## ✨ install

```bash
npm i react-hook-form
```

<br/>

## ✨ using

- `register(str)`

- `watch()`

- `handleSubmit(onValid, onInvalid)`

- `formState`

    ```typescript
    // TodoList.tsx
    import { useForm } from 'react-hook-form'
    
    const TodoList = () => {
      const { register, watch, handleSubmit, formState } = useForm()
      const onValid = (data:any) => {
        console.log(data)
      }
      return (
        <div>
          <form onSubmit={handleSubmit(onValid)}>
            <input {...register('todo', {
                required: 'todo는 필수 항목입니다.',
                minLength: {
                  value: 5,
                  message: '너무 짧습니다.'
                }
              })}
    				/>
    				<button>Add</button>
        	</form>
        </div>
      )
    }

<br/>

## ✨ 
